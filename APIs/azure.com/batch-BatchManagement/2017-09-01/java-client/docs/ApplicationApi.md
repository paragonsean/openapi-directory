# ApplicationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationCreate**](ApplicationApi.md#applicationCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationId} |  |
| [**applicationDelete**](ApplicationApi.md#applicationDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationId} |  |
| [**applicationGet**](ApplicationApi.md#applicationGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationId} |  |
| [**applicationList**](ApplicationApi.md#applicationList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications |  |
| [**applicationUpdate**](ApplicationApi.md#applicationUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationId} |  |


<a id="applicationCreate"></a>
# **applicationCreate**
> Application applicationCreate(resourceGroupName, accountName, applicationId, apiVersion, subscriptionId, parameters)



Adds an application to the specified Batch account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String applicationId = "applicationId_example"; // String | The ID of the application.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    ApplicationCreateParameters parameters = new ApplicationCreateParameters(); // ApplicationCreateParameters | The parameters for the request.
    try {
      Application result = apiInstance.applicationCreate(resourceGroupName, accountName, applicationId, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationCreate");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**ApplicationCreateParameters**](ApplicationCreateParameters.md)| The parameters for the request. | [optional] |

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The operation was successful. The response contains the application entity. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applicationDelete"></a>
# **applicationDelete**
> applicationDelete(resourceGroupName, accountName, applicationId, apiVersion, subscriptionId)



Deletes an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String applicationId = "applicationId_example"; // String | The ID of the application.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      apiInstance.applicationDelete(resourceGroupName, accountName, applicationId, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationDelete");
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

<a id="applicationGet"></a>
# **applicationGet**
> Application applicationGet(resourceGroupName, accountName, applicationId, apiVersion, subscriptionId)



Gets information about the specified application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String applicationId = "applicationId_example"; // String | The ID of the application.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      Application result = apiInstance.applicationGet(resourceGroupName, accountName, applicationId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationGet");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the application entity. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applicationList"></a>
# **applicationList**
> ListApplicationsResult applicationList(resourceGroupName, accountName, apiVersion, subscriptionId, maxresults)



Lists all of the applications in the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    Integer maxresults = 56; // Integer | The maximum number of items to return in the response.
    try {
      ListApplicationsResult result = apiInstance.applicationList(resourceGroupName, accountName, apiVersion, subscriptionId, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationList");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **maxresults** | **Integer**| The maximum number of items to return in the response. | [optional] |

### Return type

[**ListApplicationsResult**](ListApplicationsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains a list of the application entities associated with the specified account. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applicationUpdate"></a>
# **applicationUpdate**
> applicationUpdate(resourceGroupName, accountName, applicationId, apiVersion, subscriptionId, parameters)



Updates settings for the specified application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String applicationId = "applicationId_example"; // String | The ID of the application.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    ApplicationUpdateParameters parameters = new ApplicationUpdateParameters(); // ApplicationUpdateParameters | The parameters for the request.
    try {
      apiInstance.applicationUpdate(resourceGroupName, accountName, applicationId, apiVersion, subscriptionId, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationUpdate");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**ApplicationUpdateParameters**](ApplicationUpdateParameters.md)| The parameters for the request. | |

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


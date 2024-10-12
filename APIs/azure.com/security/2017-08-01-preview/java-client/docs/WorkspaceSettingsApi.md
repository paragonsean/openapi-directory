# WorkspaceSettingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspaceSettingsCreate**](WorkspaceSettingsApi.md#workspaceSettingsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName} |  |
| [**workspaceSettingsDelete**](WorkspaceSettingsApi.md#workspaceSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName} |  |
| [**workspaceSettingsGet**](WorkspaceSettingsApi.md#workspaceSettingsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName} |  |
| [**workspaceSettingsList**](WorkspaceSettingsApi.md#workspaceSettingsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings |  |
| [**workspaceSettingsUpdate**](WorkspaceSettingsApi.md#workspaceSettingsUpdate) | **PATCH** /subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName} |  |


<a id="workspaceSettingsCreate"></a>
# **workspaceSettingsCreate**
> WorkspaceSetting workspaceSettingsCreate(apiVersion, subscriptionId, workspaceSettingName, workspaceSetting)



creating settings about where we should store your security data and logs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspaceSettingsApi apiInstance = new WorkspaceSettingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String workspaceSettingName = "workspaceSettingName_example"; // String | Name of the security setting
    WorkspaceSetting workspaceSetting = new WorkspaceSetting(); // WorkspaceSetting | Security data setting object
    try {
      WorkspaceSetting result = apiInstance.workspaceSettingsCreate(apiVersion, subscriptionId, workspaceSettingName, workspaceSetting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceSettingsApi#workspaceSettingsCreate");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **workspaceSettingName** | **String**| Name of the security setting | |
| **workspaceSetting** | [**WorkspaceSetting**](WorkspaceSetting.md)| Security data setting object | |

### Return type

[**WorkspaceSetting**](WorkspaceSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workspaceSettingsDelete"></a>
# **workspaceSettingsDelete**
> workspaceSettingsDelete(apiVersion, subscriptionId, workspaceSettingName)



Deletes the custom workspace settings for this subscription. new VMs will report to the default workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspaceSettingsApi apiInstance = new WorkspaceSettingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String workspaceSettingName = "workspaceSettingName_example"; // String | Name of the security setting
    try {
      apiInstance.workspaceSettingsDelete(apiVersion, subscriptionId, workspaceSettingName);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceSettingsApi#workspaceSettingsDelete");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **workspaceSettingName** | **String**| Name of the security setting | |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workspaceSettingsGet"></a>
# **workspaceSettingsGet**
> WorkspaceSetting workspaceSettingsGet(apiVersion, subscriptionId, workspaceSettingName)



Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspaceSettingsApi apiInstance = new WorkspaceSettingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String workspaceSettingName = "workspaceSettingName_example"; // String | Name of the security setting
    try {
      WorkspaceSetting result = apiInstance.workspaceSettingsGet(apiVersion, subscriptionId, workspaceSettingName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceSettingsApi#workspaceSettingsGet");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **workspaceSettingName** | **String**| Name of the security setting | |

### Return type

[**WorkspaceSetting**](WorkspaceSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workspaceSettingsList"></a>
# **workspaceSettingsList**
> WorkspaceSettingList workspaceSettingsList(apiVersion, subscriptionId)



Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspaceSettingsApi apiInstance = new WorkspaceSettingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      WorkspaceSettingList result = apiInstance.workspaceSettingsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceSettingsApi#workspaceSettingsList");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**WorkspaceSettingList**](WorkspaceSettingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workspaceSettingsUpdate"></a>
# **workspaceSettingsUpdate**
> WorkspaceSetting workspaceSettingsUpdate(apiVersion, subscriptionId, workspaceSettingName, workspaceSetting)



Settings about where we should store your security data and logs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspaceSettingsApi apiInstance = new WorkspaceSettingsApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String workspaceSettingName = "workspaceSettingName_example"; // String | Name of the security setting
    WorkspaceSetting workspaceSetting = new WorkspaceSetting(); // WorkspaceSetting | Security data setting object
    try {
      WorkspaceSetting result = apiInstance.workspaceSettingsUpdate(apiVersion, subscriptionId, workspaceSettingName, workspaceSetting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceSettingsApi#workspaceSettingsUpdate");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **workspaceSettingName** | **String**| Name of the security setting | |
| **workspaceSetting** | [**WorkspaceSetting**](WorkspaceSetting.md)| Security data setting object | |

### Return type

[**WorkspaceSetting**](WorkspaceSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |


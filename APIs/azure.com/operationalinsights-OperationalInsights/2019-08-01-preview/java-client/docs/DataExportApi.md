# DataExportApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataExportCreateOrUpdate**](DataExportApi.md#dataExportCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataExports/{dataExportName} |  |
| [**dataExportDelete**](DataExportApi.md#dataExportDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataExports/{dataExportName} |  |
| [**dataExportGet**](DataExportApi.md#dataExportGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataExports/{dataExportName} |  |
| [**dataExportListByWorkspace**](DataExportApi.md#dataExportListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataExports |  |


<a id="dataExportCreateOrUpdate"></a>
# **dataExportCreateOrUpdate**
> DataExport dataExportCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion, parameters)



Create or update a data export.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataExportApi apiInstance = new DataExportApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The workspace's resource subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The workspace's resource group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics workspace name.
    String dataExportName = "dataExportName_example"; // String | The data export rule name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    DataExport parameters = new DataExport(); // DataExport | The parameters required to create or update a data export.
    try {
      DataExport result = apiInstance.dataExportCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExportApi#dataExportCreateOrUpdate");
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
| **subscriptionId** | **String**| The workspace&#39;s resource subscription ID. | |
| **resourceGroupName** | **String**| The workspace&#39;s resource group name. | |
| **workspaceName** | **String**| The Log Analytics workspace name. | |
| **dataExportName** | **String**| The data export rule name. | |
| **apiVersion** | **String**| The client API version. | |
| **parameters** | [**DataExport**](DataExport.md)| The parameters required to create or update a data export. | |

### Return type

[**DataExport**](DataExport.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **201** | Created response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dataExportDelete"></a>
# **dataExportDelete**
> dataExportDelete(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion)



Deletes the specified data export in a given workspace..

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataExportApi apiInstance = new DataExportApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The workspace's resource subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The workspace's resource group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics workspace name.
    String dataExportName = "dataExportName_example"; // String | The data export rule name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      apiInstance.dataExportDelete(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExportApi#dataExportDelete");
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
| **subscriptionId** | **String**| The workspace&#39;s resource subscription ID. | |
| **resourceGroupName** | **String**| The workspace&#39;s resource group name. | |
| **workspaceName** | **String**| The Log Analytics workspace name. | |
| **dataExportName** | **String**| The data export rule name. | |
| **apiVersion** | **String**| The client API version. | |

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
| **200** | OK response definition. |  -  |
| **404** | Not found the specific data export. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dataExportGet"></a>
# **dataExportGet**
> DataExport dataExportGet(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion)



Gets a data export instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataExportApi apiInstance = new DataExportApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The workspace's resource subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The workspace's resource group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics workspace name.
    String dataExportName = "dataExportName_example"; // String | The data export rule name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      DataExport result = apiInstance.dataExportGet(subscriptionId, resourceGroupName, workspaceName, dataExportName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExportApi#dataExportGet");
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
| **subscriptionId** | **String**| The workspace&#39;s resource subscription ID. | |
| **resourceGroupName** | **String**| The workspace&#39;s resource group name. | |
| **workspaceName** | **String**| The Log Analytics workspace name. | |
| **dataExportName** | **String**| The data export rule name. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**DataExport**](DataExport.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **404** | Not found the specific data export. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dataExportListByWorkspace"></a>
# **dataExportListByWorkspace**
> DataExportListResult dataExportListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion)



Lists the data export instances within a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataExportApi apiInstance = new DataExportApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The workspace's resource subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The workspace's resource group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics workspace name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      DataExportListResult result = apiInstance.dataExportListByWorkspace(subscriptionId, resourceGroupName, workspaceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataExportApi#dataExportListByWorkspace");
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
| **subscriptionId** | **String**| The workspace&#39;s resource subscription ID. | |
| **resourceGroupName** | **String**| The workspace&#39;s resource group name. | |
| **workspaceName** | **String**| The Log Analytics workspace name. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**DataExportListResult**](DataExportListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


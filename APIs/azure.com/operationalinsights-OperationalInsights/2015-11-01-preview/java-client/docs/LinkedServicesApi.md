# LinkedServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**linkedServicesCreateOrUpdate**](LinkedServicesApi.md#linkedServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/linkedServices/{linkedServiceName} |  |
| [**linkedServicesDelete**](LinkedServicesApi.md#linkedServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/linkedServices/{linkedServiceName} |  |
| [**linkedServicesGet**](LinkedServicesApi.md#linkedServicesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/linkedServices/{linkedServiceName} |  |
| [**linkedServicesListByWorkspace**](LinkedServicesApi.md#linkedServicesListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/linkedServices |  |


<a id="linkedServicesCreateOrUpdate"></a>
# **linkedServicesCreateOrUpdate**
> LinkedService linkedServicesCreateOrUpdate(resourceGroupName, workspaceName, linkedServiceName, subscriptionId, apiVersion, parameters)



Create or update a linked service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkedServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LinkedServicesApi apiInstance = new LinkedServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that will contain the linkedServices resource
    String linkedServiceName = "linkedServiceName_example"; // String | Name of the linkedServices resource
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    LinkedService parameters = new LinkedService(); // LinkedService | The parameters required to create or update a linked service.
    try {
      LinkedService result = apiInstance.linkedServicesCreateOrUpdate(resourceGroupName, workspaceName, linkedServiceName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkedServicesApi#linkedServicesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace that will contain the linkedServices resource | |
| **linkedServiceName** | **String**| Name of the linkedServices resource | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**LinkedService**](LinkedService.md)| The parameters required to create or update a linked service. | |

### Return type

[**LinkedService**](LinkedService.md)

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

<a id="linkedServicesDelete"></a>
# **linkedServicesDelete**
> linkedServicesDelete(resourceGroupName, workspaceName, linkedServiceName, apiVersion, subscriptionId)



Deletes a linked service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkedServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LinkedServicesApi apiInstance = new LinkedServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that contains the linkedServices resource
    String linkedServiceName = "linkedServiceName_example"; // String | Name of the linked service.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.linkedServicesDelete(resourceGroupName, workspaceName, linkedServiceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkedServicesApi#linkedServicesDelete");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace that contains the linkedServices resource | |
| **linkedServiceName** | **String**| Name of the linked service. | |
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
| **200** | OK response definition. |  -  |
| **204** | NoContent response definition. |  -  |

<a id="linkedServicesGet"></a>
# **linkedServicesGet**
> LinkedService linkedServicesGet(resourceGroupName, workspaceName, linkedServiceName, apiVersion, subscriptionId)



Gets a linked service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkedServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LinkedServicesApi apiInstance = new LinkedServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that contains the linkedServices resource
    String linkedServiceName = "linkedServiceName_example"; // String | Name of the linked service.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      LinkedService result = apiInstance.linkedServicesGet(resourceGroupName, workspaceName, linkedServiceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkedServicesApi#linkedServicesGet");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace that contains the linkedServices resource | |
| **linkedServiceName** | **String**| Name of the linked service. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**LinkedService**](LinkedService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="linkedServicesListByWorkspace"></a>
# **linkedServicesListByWorkspace**
> LinkedServiceListResult linkedServicesListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets the linked services instances in a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkedServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LinkedServicesApi apiInstance = new LinkedServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that contains the linked services.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      LinkedServiceListResult result = apiInstance.linkedServicesListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkedServicesApi#linkedServicesListByWorkspace");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace that contains the linked services. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**LinkedServiceListResult**](LinkedServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |


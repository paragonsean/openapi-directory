# KeysApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicesListServiceKeys_0**](KeysApi.md#servicesListServiceKeys_0) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/listkeys | Lists Service keys. |
| [**servicesRegenerateServiceKeys_0**](KeysApi.md#servicesRegenerateServiceKeys_0) | **POST** /modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/regenerateKeys | Regenerate Service Keys. |


<a id="servicesListServiceKeys_0"></a>
# **servicesListServiceKeys_0**
> AuthKeys servicesListServiceKeys_0(subscriptionId, resourceGroup, workspace, id)

Lists Service keys.

Gets a list of Service keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String id = "id_example"; // String | The Service Id.
    try {
      AuthKeys result = apiInstance.servicesListServiceKeys_0(subscriptionId, resourceGroup, workspace, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#servicesListServiceKeys_0");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **id** | **String**| The Service Id. | |

### Return type

[**AuthKeys**](AuthKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="servicesRegenerateServiceKeys_0"></a>
# **servicesRegenerateServiceKeys_0**
> AuthKeys servicesRegenerateServiceKeys_0(subscriptionId, resourceGroup, workspace, id, request)

Regenerate Service Keys.

Regenerate and return the Service keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroup = "resourceGroup_example"; // String | The Name of the resource group in which the workspace is located.
    String workspace = "workspace_example"; // String | The name of the workspace.
    String id = "id_example"; // String | The Service Id.
    RegenerateServiceKeysRequest request = new RegenerateServiceKeysRequest(); // RegenerateServiceKeysRequest | The payload that is used to regenerate keys.
    try {
      AuthKeys result = apiInstance.servicesRegenerateServiceKeys_0(subscriptionId, resourceGroup, workspace, id, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#servicesRegenerateServiceKeys_0");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroup** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspace** | **String**| The name of the workspace. | |
| **id** | **String**| The Service Id. | |
| **request** | [**RegenerateServiceKeysRequest**](RegenerateServiceKeysRequest.md)| The payload that is used to regenerate keys. | |

### Return type

[**AuthKeys**](AuthKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **202** | The request was accepted. The header &#39;Operation-Location&#39; contains the async operation location URL.  Accessing this URL with a GET call will return the status of the background task. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


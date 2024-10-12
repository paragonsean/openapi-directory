# FileContainersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fileContainersCreate**](FileContainersApi.md#fileContainersCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers/{fileContainerId} |  |
| [**fileContainersDelete**](FileContainersApi.md#fileContainersDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers/{fileContainerId} | Deletes specified file container. |
| [**fileContainersGet**](FileContainersApi.md#fileContainersGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers/{fileContainerId} |  |
| [**fileContainersList**](FileContainersApi.md#fileContainersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers |  |


<a id="fileContainersCreate"></a>
# **fileContainersCreate**
> FileContainer fileContainersCreate(subscriptionId, apiVersion, fileContainerId, fileContainerParameters)



Creates a new file container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileContainersApi apiInstance = new FileContainersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    String fileContainerId = "fileContainerId_example"; // String | The file container identifier.
    FileContainerParameters fileContainerParameters = new FileContainerParameters(); // FileContainerParameters | The parameters required to create a new file container.
    try {
      FileContainer result = apiInstance.fileContainersCreate(subscriptionId, apiVersion, fileContainerId, fileContainerParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileContainersApi#fileContainersCreate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |
| **fileContainerId** | **String**| The file container identifier. | |
| **fileContainerParameters** | [**FileContainerParameters**](FileContainerParameters.md)| The parameters required to create a new file container. | |

### Return type

[**FileContainer**](FileContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="fileContainersDelete"></a>
# **fileContainersDelete**
> fileContainersDelete(subscriptionId, fileContainerId, apiVersion)

Deletes specified file container.

Delete an existing file container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileContainersApi apiInstance = new FileContainersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String fileContainerId = "fileContainerId_example"; // String | The file container identifier.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    try {
      apiInstance.fileContainersDelete(subscriptionId, fileContainerId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileContainersApi#fileContainersDelete");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **fileContainerId** | **String**| The file container identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |

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
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="fileContainersGet"></a>
# **fileContainersGet**
> FileContainer fileContainersGet(subscriptionId, fileContainerId, apiVersion)



Retrieves the specific file container details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileContainersApi apiInstance = new FileContainersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String fileContainerId = "fileContainerId_example"; // String | The file container identifier.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    try {
      FileContainer result = apiInstance.fileContainersGet(subscriptionId, fileContainerId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileContainersApi#fileContainersGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **fileContainerId** | **String**| The file container identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |

### Return type

[**FileContainer**](FileContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="fileContainersList"></a>
# **fileContainersList**
> FileContainersList fileContainersList(subscriptionId, apiVersion)



Returns an array of file containers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileContainersApi apiInstance = new FileContainersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    try {
      FileContainersList result = apiInstance.fileContainersList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileContainersApi#fileContainersList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |

### Return type

[**FileContainersList**](FileContainersList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


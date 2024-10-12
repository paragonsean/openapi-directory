# AllowedConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allowedConnectionsGet**](AllowedConnectionsApi.md#allowedConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/allowedConnections/{connectionType} |  |
| [**allowedConnectionsList**](AllowedConnectionsApi.md#allowedConnectionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/allowedConnections |  |
| [**allowedConnectionsListByHomeRegion**](AllowedConnectionsApi.md#allowedConnectionsListByHomeRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/allowedConnections |  |


<a id="allowedConnectionsGet"></a>
# **allowedConnectionsGet**
> AllowedConnectionsResource allowedConnectionsGet(subscriptionId, resourceGroupName, ascLocation, connectionType, apiVersion)



Gets the list of all possible traffic between resources for the subscription and location, based on connection type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllowedConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AllowedConnectionsApi apiInstance = new AllowedConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String connectionType = "Internal"; // String | The type of allowed connections (Internal, External)
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      AllowedConnectionsResource result = apiInstance.allowedConnectionsGet(subscriptionId, resourceGroupName, ascLocation, connectionType, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllowedConnectionsApi#allowedConnectionsGet");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **connectionType** | **String**| The type of allowed connections (Internal, External) | [enum: Internal, External] |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**AllowedConnectionsResource**](AllowedConnectionsResource.md)

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

<a id="allowedConnectionsList"></a>
# **allowedConnectionsList**
> AllowedConnectionsList allowedConnectionsList(subscriptionId, apiVersion)



Gets the list of all possible traffic between resources for the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllowedConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AllowedConnectionsApi apiInstance = new AllowedConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      AllowedConnectionsList result = apiInstance.allowedConnectionsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllowedConnectionsApi#allowedConnectionsList");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**AllowedConnectionsList**](AllowedConnectionsList.md)

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

<a id="allowedConnectionsListByHomeRegion"></a>
# **allowedConnectionsListByHomeRegion**
> AllowedConnectionsList allowedConnectionsListByHomeRegion(subscriptionId, ascLocation, apiVersion)



Gets the list of all possible traffic between resources for the subscription and location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllowedConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AllowedConnectionsApi apiInstance = new AllowedConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      AllowedConnectionsList result = apiInstance.allowedConnectionsListByHomeRegion(subscriptionId, ascLocation, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllowedConnectionsApi#allowedConnectionsListByHomeRegion");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**AllowedConnectionsList**](AllowedConnectionsList.md)

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


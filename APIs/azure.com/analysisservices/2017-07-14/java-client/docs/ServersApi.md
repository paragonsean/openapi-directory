# ServersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serversCheckNameAvailability**](ServersApi.md#serversCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/checkNameAvailability |  |
| [**serversCreate**](ServersApi.md#serversCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName} |  |
| [**serversDelete**](ServersApi.md#serversDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName} |  |
| [**serversDissociateGateway**](ServersApi.md#serversDissociateGateway) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/dissociateGateway |  |
| [**serversGetDetails**](ServersApi.md#serversGetDetails) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName} |  |
| [**serversList**](ServersApi.md#serversList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/servers |  |
| [**serversListByResourceGroup**](ServersApi.md#serversListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers |  |
| [**serversListGatewayStatus**](ServersApi.md#serversListGatewayStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/listGatewayStatus |  |
| [**serversListOperationResults**](ServersApi.md#serversListOperationResults) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/operationresults/{operationId} |  |
| [**serversListOperationStatuses**](ServersApi.md#serversListOperationStatuses) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/operationstatuses/{operationId} |  |
| [**serversListSkusForExisting**](ServersApi.md#serversListSkusForExisting) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/skus |  |
| [**serversResume**](ServersApi.md#serversResume) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/resume |  |
| [**serversSuspend**](ServersApi.md#serversSuspend) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/suspend |  |
| [**serversUpdate**](ServersApi.md#serversUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName} |  |


<a id="serversCheckNameAvailability"></a>
# **serversCheckNameAvailability**
> CheckServerNameAvailabilityResult serversCheckNameAvailability(location, apiVersion, subscriptionId, serverParameters)



Check the name availability in the target location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String location = "location_example"; // String | The region name which the operation will lookup into.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    CheckServerNameAvailabilityParameters serverParameters = new CheckServerNameAvailabilityParameters(); // CheckServerNameAvailabilityParameters | Contains the information used to provision the Analysis Services server.
    try {
      CheckServerNameAvailabilityResult result = apiInstance.serversCheckNameAvailability(location, apiVersion, subscriptionId, serverParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversCheckNameAvailability");
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
| **location** | **String**| The region name which the operation will lookup into. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **serverParameters** | [**CheckServerNameAvailabilityParameters**](CheckServerNameAvailabilityParameters.md)| Contains the information used to provision the Analysis Services server. | |

### Return type

[**CheckServerNameAvailabilityResult**](CheckServerNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |

<a id="serversCreate"></a>
# **serversCreate**
> AnalysisServicesServer serversCreate(resourceGroupName, serverName, apiVersion, subscriptionId, serverParameters)



Provisions the specified Analysis Services server based on the configuration specified in the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    String serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    AnalysisServicesServer serverParameters = new AnalysisServicesServer(); // AnalysisServicesServer | Contains the information used to provision the Analysis Services server.
    try {
      AnalysisServicesServer result = apiInstance.serversCreate(resourceGroupName, serverName, apiVersion, subscriptionId, serverParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversCreate");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | |
| **serverName** | **String**| The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **serverParameters** | [**AnalysisServicesServer**](AnalysisServicesServer.md)| Contains the information used to provision the Analysis Services server. | |

### Return type

[**AnalysisServicesServer**](AnalysisServicesServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation completed successfully. |  -  |
| **201** | InProgress. The operation is still completing. |  -  |

<a id="serversDelete"></a>
# **serversDelete**
> serversDelete(resourceGroupName, serverName, apiVersion, subscriptionId)



Deletes the specified Analysis Services server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    String serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.serversDelete(resourceGroupName, serverName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversDelete");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | |
| **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK. |  -  |
| **202** | Accepted. |  -  |
| **204** | No Content. |  -  |

<a id="serversDissociateGateway"></a>
# **serversDissociateGateway**
> serversDissociateGateway(resourceGroupName, serverName, apiVersion, subscriptionId)



Dissociates a Unified Gateway associated with the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    String serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.serversDissociateGateway(resourceGroupName, serverName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversDissociateGateway");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | |
| **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK. |  -  |

<a id="serversGetDetails"></a>
# **serversGetDetails**
> AnalysisServicesServer serversGetDetails(resourceGroupName, serverName, apiVersion, subscriptionId)



Gets details about the specified Analysis Services server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    String serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AnalysisServicesServer result = apiInstance.serversGetDetails(resourceGroupName, serverName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversGetDetails");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | |
| **serverName** | **String**| The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AnalysisServicesServer**](AnalysisServicesServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |

<a id="serversList"></a>
# **serversList**
> AnalysisServicesServers serversList(apiVersion, subscriptionId)



Lists all the Analysis Services servers for the given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AnalysisServicesServers result = apiInstance.serversList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversList");
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AnalysisServicesServers**](AnalysisServicesServers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serversListByResourceGroup"></a>
# **serversListByResourceGroup**
> AnalysisServicesServers serversListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all the Analysis Services servers for the given resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AnalysisServicesServers result = apiInstance.serversListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AnalysisServicesServers**](AnalysisServicesServers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serversListGatewayStatus"></a>
# **serversListGatewayStatus**
> GatewayListStatusLive serversListGatewayStatus(resourceGroupName, serverName, apiVersion, subscriptionId)



Return the gateway status of the specified Analysis Services server instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    String serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      GatewayListStatusLive result = apiInstance.serversListGatewayStatus(resourceGroupName, serverName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversListGatewayStatus");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | |
| **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**GatewayListStatusLive**](GatewayListStatusLive.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | Default response as an error |  -  |

<a id="serversListOperationResults"></a>
# **serversListOperationResults**
> serversListOperationResults(location, operationId, apiVersion, subscriptionId)



List the result of the specified operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String location = "location_example"; // String | The region name which the operation will lookup into.
    String operationId = "operationId_example"; // String | The target operation Id.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.serversListOperationResults(location, operationId, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversListOperationResults");
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
| **location** | **String**| The region name which the operation will lookup into. | |
| **operationId** | **String**| The target operation Id. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK. The operation completed. |  -  |
| **202** | Accepted. The operation is ongoing. |  -  |

<a id="serversListOperationStatuses"></a>
# **serversListOperationStatuses**
> OperationStatus serversListOperationStatuses(location, operationId, apiVersion, subscriptionId)



List the status of operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String location = "location_example"; // String | The region name which the operation will lookup into.
    String operationId = "operationId_example"; // String | The target operation Id.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      OperationStatus result = apiInstance.serversListOperationStatuses(location, operationId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversListOperationStatuses");
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
| **location** | **String**| The region name which the operation will lookup into. | |
| **operationId** | **String**| The target operation Id. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation completed. |  -  |
| **202** | Accepted. The operation is ongoing. |  -  |

<a id="serversListSkusForExisting"></a>
# **serversListSkusForExisting**
> SkuEnumerationForExistingResourceResult serversListSkusForExisting(resourceGroupName, serverName, apiVersion, subscriptionId)



Lists eligible SKUs for an Analysis Services resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    String serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SkuEnumerationForExistingResourceResult result = apiInstance.serversListSkusForExisting(resourceGroupName, serverName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversListSkusForExisting");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | |
| **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SkuEnumerationForExistingResourceResult**](SkuEnumerationForExistingResourceResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serversResume"></a>
# **serversResume**
> serversResume(resourceGroupName, serverName, apiVersion, subscriptionId)



Resumes operation of the specified Analysis Services server instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    String serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.serversResume(resourceGroupName, serverName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversResume");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | |
| **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **202** | Accepted |  -  |

<a id="serversSuspend"></a>
# **serversSuspend**
> serversSuspend(resourceGroupName, serverName, apiVersion, subscriptionId)



Suspends operation of the specified Analysis Services server instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    String serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.serversSuspend(resourceGroupName, serverName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversSuspend");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | |
| **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK. |  -  |
| **202** | Accepted. |  -  |

<a id="serversUpdate"></a>
# **serversUpdate**
> AnalysisServicesServer serversUpdate(resourceGroupName, serverName, apiVersion, subscriptionId, serverUpdateParameters)



Updates the current state of the specified Analysis Services server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServersApi apiInstance = new ServersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
    String serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    AnalysisServicesServerUpdateParameters serverUpdateParameters = new AnalysisServicesServerUpdateParameters(); // AnalysisServicesServerUpdateParameters | Request object that contains the updated information for the server.
    try {
      AnalysisServicesServer result = apiInstance.serversUpdate(resourceGroupName, serverName, apiVersion, subscriptionId, serverUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServersApi#serversUpdate");
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
| **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | |
| **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **serverUpdateParameters** | [**AnalysisServicesServerUpdateParameters**](AnalysisServicesServerUpdateParameters.md)| Request object that contains the updated information for the server. | |

### Return type

[**AnalysisServicesServer**](AnalysisServicesServer.md)

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


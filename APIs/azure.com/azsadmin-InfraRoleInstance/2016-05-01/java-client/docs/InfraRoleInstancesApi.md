# InfraRoleInstancesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**infraRoleInstancesGet**](InfraRoleInstancesApi.md#infraRoleInstancesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances/{infraRoleInstance} |  |
| [**infraRoleInstancesList**](InfraRoleInstancesApi.md#infraRoleInstancesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances |  |
| [**infraRoleInstancesPowerOff**](InfraRoleInstancesApi.md#infraRoleInstancesPowerOff) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances/{infraRoleInstance}/PowerOff |  |
| [**infraRoleInstancesPowerOn**](InfraRoleInstancesApi.md#infraRoleInstancesPowerOn) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances/{infraRoleInstance}/PowerOn |  |
| [**infraRoleInstancesReboot**](InfraRoleInstancesApi.md#infraRoleInstancesReboot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances/{infraRoleInstance}/Reboot |  |
| [**infraRoleInstancesShutdown**](InfraRoleInstancesApi.md#infraRoleInstancesShutdown) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances/{infraRoleInstance}/Shutdown |  |


<a id="infraRoleInstancesGet"></a>
# **infraRoleInstancesGet**
> InfraRoleInstance infraRoleInstancesGet(subscriptionId, resourceGroupName, location, infraRoleInstance, apiVersion)



Return the requested infrastructure role instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfraRoleInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InfraRoleInstancesApi apiInstance = new InfraRoleInstancesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String infraRoleInstance = "infraRoleInstance_example"; // String | Name of an infrastructure role instance.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      InfraRoleInstance result = apiInstance.infraRoleInstancesGet(subscriptionId, resourceGroupName, location, infraRoleInstance, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfraRoleInstancesApi#infraRoleInstancesGet");
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
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **infraRoleInstance** | **String**| Name of an infrastructure role instance. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

### Return type

[**InfraRoleInstance**](InfraRoleInstance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="infraRoleInstancesList"></a>
# **infraRoleInstancesList**
> InfraRoleInstanceList infraRoleInstancesList(subscriptionId, resourceGroupName, location, apiVersion, $filter)



Returns a list of all infrastructure role instances at a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfraRoleInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InfraRoleInstancesApi apiInstance = new InfraRoleInstancesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    String $filter = "$filter_example"; // String | OData filter parameter.
    try {
      InfraRoleInstanceList result = apiInstance.infraRoleInstancesList(subscriptionId, resourceGroupName, location, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfraRoleInstancesApi#infraRoleInstancesList");
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
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |
| **$filter** | **String**| OData filter parameter. | [optional] |

### Return type

[**InfraRoleInstanceList**](InfraRoleInstanceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="infraRoleInstancesPowerOff"></a>
# **infraRoleInstancesPowerOff**
> infraRoleInstancesPowerOff(subscriptionId, resourceGroupName, location, infraRoleInstance, apiVersion)



Power off an infrastructure role instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfraRoleInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InfraRoleInstancesApi apiInstance = new InfraRoleInstancesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String infraRoleInstance = "infraRoleInstance_example"; // String | Name of an infrastructure role instance.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      apiInstance.infraRoleInstancesPowerOff(subscriptionId, resourceGroupName, location, infraRoleInstance, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfraRoleInstancesApi#infraRoleInstancesPowerOff");
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
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **infraRoleInstance** | **String**| Name of an infrastructure role instance. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

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
| **202** | ACCEPTED |  -  |

<a id="infraRoleInstancesPowerOn"></a>
# **infraRoleInstancesPowerOn**
> infraRoleInstancesPowerOn(subscriptionId, resourceGroupName, location, infraRoleInstance, apiVersion)



Power on an infrastructure role instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfraRoleInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InfraRoleInstancesApi apiInstance = new InfraRoleInstancesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String infraRoleInstance = "infraRoleInstance_example"; // String | Name of an infrastructure role instance.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      apiInstance.infraRoleInstancesPowerOn(subscriptionId, resourceGroupName, location, infraRoleInstance, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfraRoleInstancesApi#infraRoleInstancesPowerOn");
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
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **infraRoleInstance** | **String**| Name of an infrastructure role instance. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

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
| **202** | ACCEPTED |  -  |

<a id="infraRoleInstancesReboot"></a>
# **infraRoleInstancesReboot**
> infraRoleInstancesReboot(subscriptionId, resourceGroupName, location, infraRoleInstance, apiVersion)



Reboot an infrastructure role instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfraRoleInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InfraRoleInstancesApi apiInstance = new InfraRoleInstancesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String infraRoleInstance = "infraRoleInstance_example"; // String | Name of an infrastructure role instance.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      apiInstance.infraRoleInstancesReboot(subscriptionId, resourceGroupName, location, infraRoleInstance, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfraRoleInstancesApi#infraRoleInstancesReboot");
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
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **infraRoleInstance** | **String**| Name of an infrastructure role instance. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

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
| **202** | ACCEPTED |  -  |

<a id="infraRoleInstancesShutdown"></a>
# **infraRoleInstancesShutdown**
> infraRoleInstancesShutdown(subscriptionId, resourceGroupName, location, infraRoleInstance, apiVersion)



Shut down an infrastructure role instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfraRoleInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InfraRoleInstancesApi apiInstance = new InfraRoleInstancesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String location = "location_example"; // String | Location of the resource.
    String infraRoleInstance = "infraRoleInstance_example"; // String | Name of an infrastructure role instance.
    String apiVersion = "2016-05-01"; // String | Client API Version.
    try {
      apiInstance.infraRoleInstancesShutdown(subscriptionId, resourceGroupName, location, infraRoleInstance, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfraRoleInstancesApi#infraRoleInstancesShutdown");
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
| **resourceGroupName** | **String**| Name of the resource group. | |
| **location** | **String**| Location of the resource. | |
| **infraRoleInstance** | **String**| Name of an infrastructure role instance. | |
| **apiVersion** | **String**| Client API Version. | [default to 2016-05-01] |

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
| **202** | ACCEPTED |  -  |


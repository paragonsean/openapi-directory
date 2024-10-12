# DeviceServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicesCreateOrUpdate**](DeviceServicesApi.md#servicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsIoT/deviceServices/{deviceName} | Create or update the metadata of a Windows IoT Device Service. |
| [**servicesDelete**](DeviceServicesApi.md#servicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsIoT/deviceServices/{deviceName} |  |
| [**servicesGet**](DeviceServicesApi.md#servicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsIoT/deviceServices/{deviceName} |  |
| [**servicesList**](DeviceServicesApi.md#servicesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.WindowsIoT/deviceServices |  |
| [**servicesListByResourceGroup**](DeviceServicesApi.md#servicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsIoT/deviceServices |  |
| [**servicesUpdate**](DeviceServicesApi.md#servicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsIoT/deviceServices/{deviceName} | Updates the metadata of a Windows IoT Device Service. |


<a id="servicesCreateOrUpdate"></a>
# **servicesCreateOrUpdate**
> DeviceService servicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, deviceName, deviceService, ifMatch)

Create or update the metadata of a Windows IoT Device Service.

Create or update the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeviceServicesApi apiInstance = new DeviceServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Windows IoT Device Service.
    String deviceName = "deviceName_example"; // String | The name of the Windows IoT Device Service.
    DeviceService deviceService = new DeviceService(); // DeviceService | The Windows IoT Device Service metadata and security metadata.
    String ifMatch = "ifMatch_example"; // String | ETag of the Windows IoT Device Service. Do not specify for creating a new Windows IoT Device Service. Required to update an existing Windows IoT Device Service.
    try {
      DeviceService result = apiInstance.servicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, deviceName, deviceService, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceServicesApi#servicesCreateOrUpdate");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the Windows IoT Device Service. | |
| **deviceName** | **String**| The name of the Windows IoT Device Service. | |
| **deviceService** | [**DeviceService**](DeviceService.md)| The Windows IoT Device Service metadata and security metadata. | |
| **ifMatch** | **String**| ETag of the Windows IoT Device Service. Do not specify for creating a new Windows IoT Device Service. Required to update an existing Windows IoT Device Service. | [optional] |

### Return type

[**DeviceService**](DeviceService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="servicesDelete"></a>
# **servicesDelete**
> DeviceService servicesDelete(apiVersion, subscriptionId, resourceGroupName, deviceName)



Delete a Windows IoT Device Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeviceServicesApi apiInstance = new DeviceServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Windows IoT Device Service.
    String deviceName = "deviceName_example"; // String | The name of the Windows IoT Device Service.
    try {
      DeviceService result = apiInstance.servicesDelete(apiVersion, subscriptionId, resourceGroupName, deviceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceServicesApi#servicesDelete");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the Windows IoT Device Service. | |
| **deviceName** | **String**| The name of the Windows IoT Device Service. | |

### Return type

[**DeviceService**](DeviceService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="servicesGet"></a>
# **servicesGet**
> DeviceService servicesGet(apiVersion, subscriptionId, resourceGroupName, deviceName)



Get the non-security related metadata of a Windows IoT Device Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeviceServicesApi apiInstance = new DeviceServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Windows IoT Device Service.
    String deviceName = "deviceName_example"; // String | The name of the Windows IoT Device Service.
    try {
      DeviceService result = apiInstance.servicesGet(apiVersion, subscriptionId, resourceGroupName, deviceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceServicesApi#servicesGet");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the Windows IoT Device Service. | |
| **deviceName** | **String**| The name of the Windows IoT Device Service. | |

### Return type

[**DeviceService**](DeviceService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="servicesList"></a>
# **servicesList**
> DeviceServiceDescriptionListResult servicesList(apiVersion, subscriptionId)



Get all the IoT hubs in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeviceServicesApi apiInstance = new DeviceServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    try {
      DeviceServiceDescriptionListResult result = apiInstance.servicesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceServicesApi#servicesList");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |

### Return type

[**DeviceServiceDescriptionListResult**](DeviceServiceDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="servicesListByResourceGroup"></a>
# **servicesListByResourceGroup**
> DeviceServiceDescriptionListResult servicesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all the IoT hubs in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeviceServicesApi apiInstance = new DeviceServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Windows IoT Device Service.
    try {
      DeviceServiceDescriptionListResult result = apiInstance.servicesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceServicesApi#servicesListByResourceGroup");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the Windows IoT Device Service. | |

### Return type

[**DeviceServiceDescriptionListResult**](DeviceServiceDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="servicesUpdate"></a>
# **servicesUpdate**
> DeviceService servicesUpdate(apiVersion, subscriptionId, resourceGroupName, deviceName, deviceService, ifMatch)

Updates the metadata of a Windows IoT Device Service.

Updates the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeviceServicesApi apiInstance = new DeviceServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Windows IoT Device Service.
    String deviceName = "deviceName_example"; // String | The name of the Windows IoT Device Service.
    DeviceService deviceService = new DeviceService(); // DeviceService | The Windows IoT Device Service metadata and security metadata.
    String ifMatch = "ifMatch_example"; // String | ETag of the Windows IoT Device Service. Do not specify for creating a brand new Windows IoT Device Service. Required to update an existing Windows IoT Device Service.
    try {
      DeviceService result = apiInstance.servicesUpdate(apiVersion, subscriptionId, resourceGroupName, deviceName, deviceService, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceServicesApi#servicesUpdate");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the Windows IoT Device Service. | |
| **deviceName** | **String**| The name of the Windows IoT Device Service. | |
| **deviceService** | [**DeviceService**](DeviceService.md)| The Windows IoT Device Service metadata and security metadata. | |
| **ifMatch** | **String**| ETag of the Windows IoT Device Service. Do not specify for creating a brand new Windows IoT Device Service. Required to update an existing Windows IoT Device Service. | [optional] |

### Return type

[**DeviceService**](DeviceService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | DefaultErrorResponse |  -  |


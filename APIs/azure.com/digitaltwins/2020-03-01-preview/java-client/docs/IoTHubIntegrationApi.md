# IoTHubIntegrationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**digitalTwinsIoTHubsList**](IoTHubIntegrationApi.md#digitalTwinsIoTHubsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName}/integrationResources |  |
| [**ioTHubCreateOrUpdate**](IoTHubIntegrationApi.md#ioTHubCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.DigitalTwins/integrationResources/{integrationResourceName} |  |
| [**ioTHubDelete**](IoTHubIntegrationApi.md#ioTHubDelete) | **DELETE** /{scope}/providers/Microsoft.DigitalTwins/integrationResources/{integrationResourceName} |  |
| [**ioTHubGet**](IoTHubIntegrationApi.md#ioTHubGet) | **GET** /{scope}/providers/Microsoft.DigitalTwins/integrationResources/{integrationResourceName} |  |


<a id="digitalTwinsIoTHubsList"></a>
# **digitalTwinsIoTHubsList**
> DigitalTwinsIntegrationResourceListResult digitalTwinsIoTHubsList(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get DigitalTwinsInstance IoTHubs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTHubIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTHubIntegrationApi apiInstance = new IoTHubIntegrationApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
    String resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
    try {
      DigitalTwinsIntegrationResourceListResult result = apiInstance.digitalTwinsIoTHubsList(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTHubIntegrationApi#digitalTwinsIoTHubsList");
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
| **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | [enum: 2020-03-01-preview] |
| **subscriptionId** | **UUID**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | |
| **resourceName** | **String**| The name of the DigitalTwinsInstance. | |

### Return type

[**DigitalTwinsIntegrationResourceListResult**](DigitalTwinsIntegrationResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains all the non-security properties of the DigitalTwinsInstance. Security-related properties are set to null. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ioTHubCreateOrUpdate"></a>
# **ioTHubCreateOrUpdate**
> IntegrationResource ioTHubCreateOrUpdate(scope, integrationResourceName, iotHubDescription)



Creates or Updates an IoTHub Integration with DigitalTwinsInstances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTHubIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTHubIntegrationApi apiInstance = new IoTHubIntegrationApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}.
    String integrationResourceName = "integrationResourceName_example"; // String | Name of IoTHub and DigitalTwinsInstance integration instance.
    IntegrationResource iotHubDescription = new IntegrationResource(); // IntegrationResource | The IoTHub metadata.
    try {
      IntegrationResource result = apiInstance.ioTHubCreateOrUpdate(scope, integrationResourceName, iotHubDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTHubIntegrationApi#ioTHubCreateOrUpdate");
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
| **scope** | **String**| The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}. | |
| **integrationResourceName** | **String**| Name of IoTHub and DigitalTwinsInstance integration instance. | |
| **iotHubDescription** | [**IntegrationResource**](IntegrationResource.md)| The IoTHub metadata. | |

### Return type

[**IntegrationResource**](IntegrationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | This is an asynchronous operation. The body contains metadata about IoTHub and DigitalTwinsInstance Integration. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ioTHubDelete"></a>
# **ioTHubDelete**
> ioTHubDelete(scope, integrationResourceName)



Deletes a DigitalTwinsInstance link with IoTHub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTHubIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTHubIntegrationApi apiInstance = new IoTHubIntegrationApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}.
    String integrationResourceName = "integrationResourceName_example"; // String | Name of IoTHub and DigitalTwinsInstance integration instance.
    try {
      apiInstance.ioTHubDelete(scope, integrationResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTHubIntegrationApi#ioTHubDelete");
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
| **scope** | **String**| The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}. | |
| **integrationResourceName** | **String**| Name of IoTHub and DigitalTwinsInstance integration instance. | |

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
| **200** | OK. DigitalTwinsInstance IoTHub link has been Deleted. |  -  |
| **202** | Accepted. Response includes a Location header which points to the DigitalTwins and IoTHub Integration resource. |  -  |
| **204** | NoContent. DigitalTwinsInstance IoTHub link does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ioTHubGet"></a>
# **ioTHubGet**
> IntegrationResource ioTHubGet(scope, integrationResourceName)



Gets properties of an IoTHub Integration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTHubIntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTHubIntegrationApi apiInstance = new IoTHubIntegrationApi(defaultClient);
    String scope = "scope_example"; // String | The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}.
    String integrationResourceName = "integrationResourceName_example"; // String | Name of IoTHub and DigitalTwinsInstance integration instance.
    try {
      IntegrationResource result = apiInstance.ioTHubGet(scope, integrationResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTHubIntegrationApi#ioTHubGet");
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
| **scope** | **String**| The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}. | |
| **integrationResourceName** | **String**| Name of IoTHub and DigitalTwinsInstance integration instance. | |

### Return type

[**IntegrationResource**](IntegrationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains metadata about IoTHub and DigitalTwinsInstance Integration. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


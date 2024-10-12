# EndpointsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**digitalTwinsEndpointCreateOrUpdate**](EndpointsApi.md#digitalTwinsEndpointCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName}/endpoints/{endpointName} |  |
| [**digitalTwinsEndpointDelete**](EndpointsApi.md#digitalTwinsEndpointDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName}/endpoints/{endpointName} |  |
| [**digitalTwinsEndpointGet**](EndpointsApi.md#digitalTwinsEndpointGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName}/endpoints/{endpointName} |  |
| [**digitalTwinsEndpointList**](EndpointsApi.md#digitalTwinsEndpointList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName}/endpoints |  |


<a id="digitalTwinsEndpointCreateOrUpdate"></a>
# **digitalTwinsEndpointCreateOrUpdate**
> DigitalTwinsEndpointResource digitalTwinsEndpointCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName, endpointDescription)



Create or update DigitalTwinsInstance endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
    String resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
    String endpointName = "endpointName_example"; // String | Name of Endpoint Resource.
    DigitalTwinsEndpointResource endpointDescription = new DigitalTwinsEndpointResource(); // DigitalTwinsEndpointResource | The DigitalTwinsInstance endpoint metadata and security metadata.
    try {
      DigitalTwinsEndpointResource result = apiInstance.digitalTwinsEndpointCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName, endpointDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#digitalTwinsEndpointCreateOrUpdate");
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
| **endpointName** | **String**| Name of Endpoint Resource. | |
| **endpointDescription** | [**DigitalTwinsEndpointResource**](DigitalTwinsEndpointResource.md)| The DigitalTwinsInstance endpoint metadata and security metadata. | |

### Return type

[**DigitalTwinsEndpointResource**](DigitalTwinsEndpointResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is returned as a response to the status polling request for the create or update operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **201** | Created - Put request accepted; the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="digitalTwinsEndpointDelete"></a>
# **digitalTwinsEndpointDelete**
> digitalTwinsEndpointDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName)



Delete a DigitalTwinsInstance endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
    String resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
    String endpointName = "endpointName_example"; // String | Name of Endpoint Resource.
    try {
      apiInstance.digitalTwinsEndpointDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#digitalTwinsEndpointDelete");
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
| **endpointName** | **String**| Name of Endpoint Resource. | |

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
| **200** | This is returned as a response to the status polling request for the delete operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **202** | Accepted - Delete request accepted; the operation will complete asynchronously. |  -  |
| **204** | Once the long running delete operation completes successfully, a 204 No Content status code is returned when the status polling request finds the DigitalTwins service metadata in the service and the status of the delete operation is set to a completed state. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="digitalTwinsEndpointGet"></a>
# **digitalTwinsEndpointGet**
> DigitalTwinsEndpointResource digitalTwinsEndpointGet(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName)



Get DigitalTwinsInstances Endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
    String resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
    String endpointName = "endpointName_example"; // String | Name of Endpoint Resource.
    try {
      DigitalTwinsEndpointResource result = apiInstance.digitalTwinsEndpointGet(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#digitalTwinsEndpointGet");
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
| **endpointName** | **String**| Name of Endpoint Resource. | |

### Return type

[**DigitalTwinsEndpointResource**](DigitalTwinsEndpointResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains all the non-security properties of the DigitalTwinsInstance. Security-related properties are set to null. |  -  |
| **0** | Default error response |  -  |

<a id="digitalTwinsEndpointList"></a>
# **digitalTwinsEndpointList**
> DigitalTwinsEndpointResourceListResult digitalTwinsEndpointList(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get DigitalTwinsInstance Endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String apiVersion = "2020-03-01-preview"; // String | Version of the DigitalTwinsInstance Management API.
    UUID subscriptionId = UUID.randomUUID(); // UUID | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
    String resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
    try {
      DigitalTwinsEndpointResourceListResult result = apiInstance.digitalTwinsEndpointList(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#digitalTwinsEndpointList");
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

[**DigitalTwinsEndpointResourceListResult**](DigitalTwinsEndpointResourceListResult.md)

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

